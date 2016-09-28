#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import random


products = [
    {
        'name': 'Humvee Pilot Sunglasses, Grey Polarized Lens, Black Frame 52 mm',
        'price': 16.99,
        'sale-tax': 0,
        'shipping-cost': 0,
        'declared-price': 8,
        'weight': 0.05,
        'tracking-code': 'LeisurePro'
    },{
        'name': 'Blue Reef Orca Torch 700 Lumen LED Dive Light Kit',
        'price': 99.95,
        'sale-tax': 0,
        'shipping-cost': 0,
        'declared-price': 42.99,
        'weight': 2.3,
        'tracking-code': 'LeisurePro'
    }
]


class ShippingOrderItem(object):

    def __init__(self, product):
        self.product = product

    def get_tracking_code(self):
        return self.product['tracking-code']

    def get_price(self):
        return self.product['price'] + self.product['sale-tax']

    def get_shipping_cost(self):
        return self.product['shipping-cost']

    def get_weight(self):
        return self.product['weight']

    def get_cif(self):
        return self.get_price() + self.get_shipping_cost()

    def get_declared_price(self):
        return self.product['declared-price']

    def get_tariff(self):
        return 0.1 * self.get_declared_price()

    def get_vat(self):
        return 0.16 * (self.get_declared_price() + self.get_tariff())

    def get_taxes(self):
        return self.get_tariff() + self.get_vat()


class ShippingOrder(object):

    def __init__(self, items):
        self.items = items

    def get_taxes(self):
        declared_price = sum([i.get_declared_price() for i in self.items])

        if declared_price <= 200:
            taxes = sum([i.get_tariff() for i in self.items])
        else:
            taxes = sum([i.get_tariff() + i.get_vat() for i in self.items])

        return taxes

    def get_shipping_cost(self):
        weight = sum([i.get_weight() for i in self.items])

        if weight < 6.0:
            shipping_cost = 16
        elif weight < 15:
            shipping_cost = 16 + (weight - 6) * 2.75
        else:
            shipping_cost = 16 + (weight - 6) * 2.50

        return shipping_cost

    def get_insurance_cost(self):
        declared_price = sum([i.get_declared_price() for i in self.items])
        return max(declared_price * 0.015, 1.5)

    def get_logistics_costs(self):
        tracking_codes = set([i.get_tracking_code() for i in self.items])
        return 2.0 * len(tracking_codes)

    def get_fuel_surcharge(self):
        weight = sum([i.get_weight() for i in self.items])

        if weight < 9:
            surcharge = 1
        elif weight < 29:
            surcharge = 2
        elif weight < 59:
            surcharge = 3
        else:
            surcharge = 4

        return surcharge

    def get_subtotal(self):
        invoice_items = [
            self.get_taxes(),
            self.get_shipping_cost(),
            self.get_insurance_cost(),
            self.get_logistics_costs(),
            self.get_fuel_surcharge()
        ]

        return sum(invoice_items)

    def get_credit_card_surcharge(self):
        return 0.035 * self.get_subtotal()

    def get_total(self):
        return self.get_subtotal() + self.get_credit_card_surcharge()

class ShippingOrdersGenerator(object):

    max_iterations = 800
    max_solutions = 16
    mutation_p = 0.8

    def get_shipping_orders(self, products):
        order_items = self.create_shipping_order_items(products)

        declared_price = sum([item.get_declared_price() for item in order_items])
        weight = sum([item.get_weight() for item in order_items])

        max_shipping_orders_by_cost = math.ceil(declared_price / 200)
        max_shipping_orders_by_weight = math.ceil(weight / 6 )
        max_shipping_orders = int(max(max_shipping_orders_by_cost, max_shipping_orders_by_weight))

        solutions = [self.generate_initial_solution(len(order_items), max_shipping_orders)]

        iterations = 0

        # print iterations
        # print '\n'.join([str(s) for s in solutions])

        while iterations < self.max_iterations:
            solutions = self.generate_next_solutions(solutions, order_items, self.max_solutions, max_shipping_orders)
            iterations = iterations + 1
            # print iterations
            # print '\n'.join([str(s) for s in solutions])

        return self.get_shipping_orders_from_solution(solutions[0], order_items)

    def create_shipping_order_items(self, products):
        return [ShippingOrderItem(product) for product in products]

    def generate_initial_solution(self, item_count, max_shipping_orders):
        solution = []

        for i in range(0, item_count):
            # solution.append(random.randint(0, max_shipping_orders))
            solution.append(0)

        return solution

    def generate_next_solutions(self, solutions, order_items, max_solutions, max_shipping_orders):
        new_solutions = solutions + self.mutate_solutions(solutions, max_shipping_orders)
        new_solutions = dict([(self.get_solution_fingerprint(s), s) for s in new_solutions]).values()
        new_solutions = self.sort_solutions(new_solutions, order_items)

        good_solutions_count = max(int(math.floor(max_solutions / 3)), 1)
        random_solutions_count = min(max(len(new_solutions) - good_solutions_count, 0), max_solutions - good_solutions_count)

        good_solutions = new_solutions[0:good_solutions_count]
        random_solutions = random.sample(new_solutions[good_solutions_count:], random_solutions_count)
        # print "good"
        # print '\n'.join([str(s) for s in good_solutions])

        # print "random"
        # print '\n'.join([str(s) for s in random_solutions])

        return good_solutions + random_solutions

    def mutate_solutions(self, solutions, max_shipping_orders):
        new_solutions = []

        for solution in solutions:
            new_solution = []
            mutation = []

            for entry in solution:
                if random.random() < self.mutation_p:
                    mutation.append("C")
                    new_solution.append((entry + 1) % max_shipping_orders)
                else:
                    new_solution.append(entry)
                    mutation.append("N")

            # print mutation

            new_solutions.append(new_solution)

        return new_solutions

    def sort_solutions(self, solutions, order_items):
        costs = [(s, self.calculate_solution_cost(s, order_items)) for s in solutions]
        costs.sort(key=lambda pair: pair[1])

        return [pair[0] for pair in costs]

    def calculate_solution_cost(self, solution, order_items):
        shipping_orders = self.get_shipping_orders_from_solution(solution, order_items)

        return sum([shipping_order.get_total() for shipping_order in shipping_orders])

    def get_shipping_orders_from_solution(self, solution, order_items):
        shipping_orders_items = {}

        for i, entry in enumerate(solution):
            if entry not in shipping_orders_items:
                shipping_orders_items[entry] = [order_items[i]]
            else:
                shipping_orders_items[entry].append(order_items[i])

        shipping_orders = []

        for shipping_order_number in shipping_orders_items:
            shipping_orders.append(ShippingOrder(shipping_orders_items[shipping_order_number]))

        return shipping_orders

    def get_solution_fingerprint(self, solution):
        return '-'.join([str(entry) for entry in solution])


def main():
    generator = ShippingOrdersGenerator()
    shipping_orders = generator.get_shipping_orders(products)
    grand_total = 0

    for i, shipping_order in enumerate(shipping_orders):
        print("Shipping Order #{0}".format(i))

        for item in shipping_order.items:
            print("- {0}".format(item.product['name']))

        order_total = shipping_order.get_total()
        grand_total = grand_total + order_total

        print("Total: {0}".format(order_total))
        print("")

    print("Grand Total: {0}".format(grand_total))

if __name__ == '__main__':
    main()
