#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import random


TRM = 3070.54
products = [
    {
        'name': '[W] Princeton Tec Meridian Strobe',
        'price': 29.99,
        'sale-tax': 0,
        'shipping-cost': 0,
        'declared-price': 14.99,
        'weight': 0.5,
        'tracking-code': 'PTCMS'
    },{
        'name': '[W] Trident Divemaster Underwater LED Strobe',
        'price': 44.99,
        'sale-tax': 0,
        'shipping-cost': 6.49,
        'declared-price': 22.5,
        'weight': 1,
        'tracking-code': 'TDULS'
    },{
        'name': '[W] AQUATEC Diving Duo-Alert',
        'price': 59.95,
        'sale-tax': 0,
        'shipping-cost': 6.95,
        'declared-price': 27.5,
        'weight': 1,
        'tracking-code': 'ADDA'
    },{
        'name': '[W] Aquacraft Aluminum Scuba Diving Noise Signal',
        'price': 19.75,
        'sale-tax': 0,
        'shipping-cost': 0,
        'declared-price': 10,
        'weight': 0.22,
        'tracking-code': 'AASDNS'
#    },{
#        'name': 'Mares Magnetic Shaker Accessory',
#        'price': 25.97,
#        'sale-tax': 0,
#        'shipping-cost': 0,
#        'declared-price': 12.99,
#        'weight': 0.18,
#        'tracking-code': 'MMSA'
    },{
        'name': '[W] Finger Reel with Brass Clip (160ft)',
        'price': 14,
        'sale-tax': 0,
        'shipping-cost': 0,
        'declared-price': 7,
        'weight': 0.5,
        'tracking-code': 'FRBC160'
#    },{
#        'name': 'XS Scuba Highland 10 ft. SMB',
#        'price': 88.95,
#        'sale-tax': 0,
#        'shipping-cost': 0,
#        'declared-price': 44.99,
#        'weight': 2,
#        'tracking-code': 'FRBC160'
#    },{
#        'name': '[W] Scuba Choice 6 ft Oral and Standard BC Hose Inflator',
#        'price': 26.45,
#        'sale-tax': 0,
#        'shipping-cost': 0,
#        'declared-price': 13.5,
#        'weight': 0.25,
#        'tracking-code': 'SC6OSBCHI'
#    },{
#        'name': 'Scuba Diving Tank O-Ring Dive Kit Keychain with Pick',
#        'price': 12.5,
#        'sale-tax': 0,
#        'shipping-cost': 0,
#        'declared-price': 6.25,
#        'weight': 0.019,
#        'tracking-code': 'SDTODKKP'
    },{
        'name': '[W] ACR Signaling Mirror',
        'price': 15.83,
        'sale-tax': 0,
        'shipping-cost': 0,
        'declared-price': 7.57,
        'weight': 0.15,
        'tracking-code': 'ACRSM'
    },{
        'name': '[W] Aduro U-GRIP Universal Mount',
        'price': 19.95,
        'sale-tax': 0,
        'shipping-cost': 0,
        'declared-price': 10,
        'weight': 0.2,
        'tracking-code': 'AUGRIPUM'
    },{
        'name': '[W] Pilot Juice Gel Ink Ballpoint Pen, 0.38 mm',
        'price': 13.80,
        'sale-tax': 0,
        'shipping-cost': 0,
        'declared-price': 7,
        'weight': 0.28,
        'tracking-code': 'PJGIBP038MM'
    },{
        'name': '[W] Scuba Choice 6 ft Oral and Standard BC Hose Inflator*',
        'price': 45,
        'sale-tax': 3.15,
        'shipping-cost': 0,
        'declared-price': 24.08,
        'weight': 0.07,
        'tracking-code': 'TIMB'
    },{
        'name': '[J] Alice in Wonderland Pocket Watch Infinity Scarf',
        'price': 9.99,
        'sale-tax': 0.7,
        'shipping-cost': 0,
        'declared-price': 4.99,
        'weight': 0.11,
        'tracking-code': 'AWPWIS'
    },{
        'name': '[J] Anime May the Force Be With You Ladies Hoodie - Black, M',
        'price': 49.99,
        'sale-tax': 3.5,
        'shipping-cost': 0,
        'declared-price': 26.5,
        'weight': 0.88,
        'tracking-code': 'AMFBWYLH'
    },{
        'name': '[J] Plush Zombie Slippers',
        'price': 9.99,
        'sale-tax': 0.7,
        'shipping-cost': 0,
        'declared-price': 4.99,
        'weight': 0.75,
        'tracking-code': 'PZS'
    },{
        'name': '[J] The Flash Cuff Beanie',
        'price': 19.99,
        'sale-tax': 1.39,
        'shipping-cost': 0,
        'declared-price': 10.99,
        'weight': 0.15,
        'tracking-code': 'PJGIBP038MM'
    },{
        'name': '[A] (!) One Night Ultimate Werewolf',
        'price': 13.59,
        'sale-tax': 0.00,
        'shipping-cost': 0,
        'declared-price': 6.5,
        'weight': 0.48,
        'tracking-code': 'ONUW'
    },{
        'name': '[A] (NO) Zombie Dice',
        'price': 11.20,
        'sale-tax': 0.00,
        'shipping-cost': 0,
        'declared-price': 6,
        'weight': 0.38,
        'tracking-code': 'ZD'
    },{
        'name': '[A] Forbidden Island',
        'price': 12.99,
        'sale-tax': 0.00,
        'shipping-cost': 0,
        'declared-price': 6.49,
        'weight': 1.4,
        'tracking-code': 'FI'
    },{
        'name': '[A] Smash Up Game',
        'price': 18.99,
        'sale-tax': 0.00,
        'shipping-cost': 0,
        'declared-price': 8.49,
        'weight': 1.6,
        'tracking-code': 'SUG'
    },{
        'name': '[A] Sushi Go! - The Pick and Pass Card Game',
        'price': 8.57,
        'sale-tax': 0.00,
        'shipping-cost': 0,
        'declared-price': 4.25,
        'weight': 0.81,
        'tracking-code': 'SGTPAPCC'
    },{
        'name': '[D] iPhone 5 5S SE screen protector',
        'price': 6.95,
        'sale-tax': 0.00,
        'shipping-cost': 0,
        'declared-price': 3.5,
        'weight': 0.06,
        'tracking-code': 'i5SSP'
    },{
        'name': '[D] ANGELLA-M Case For Apple iphone 5 5S Beautiful Flower',
        'price': 0.01,
        'sale-tax': 0.00,
        'shipping-cost': 4.99,
        'declared-price': 1.99,
        'weight': 0.07,
        'tracking-code': 'ACFAi5SBF'
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

        shipping_costs = shipping_order.get_shipping_cost() + shipping_order.get_logistics_costs() + shipping_order.get_fuel_surcharge()
        other_costs = shipping_order.get_taxes() + shipping_order.get_credit_card_surcharge() + shipping_order.get_insurance_cost()

        total_cost = sum([i.get_cif() for i in shipping_order.items])
        total_weight = sum([i.get_weight() for i in shipping_order.items])

        print("  {0: <60s} {1: >9}   {2: >7}   {3: >8}   {4: >7}   {5: >7}   {6: >7}".format(
            '',
            'Weight',
            'CIF',
            'Shipping',
            'Taxes*',
            'Total',
            'Total (COP)'
        ))

        for item in shipping_order.items:
            shipping_ratio = item.get_weight() / total_weight
            cost_ratio = item.get_cif() / total_cost

            item_shipping_cost = shipping_ratio * shipping_costs
            item_other_cost = cost_ratio * other_costs

            item_cost = item.get_cif() + item_shipping_cost + item_other_cost

            print("- {0: <60s} {1: >6.2f} lb   ${2: >6.2f}   ${3: >7.2f}   ${4: >6.2f}   ${5: >6.2f}   COP {6}".format(
                item.product['name'][0:60],
                item.get_weight(),
                item.get_cif(),
                item_shipping_cost,
                item_other_cost,
                item_cost,
                '{0: >7,.0f}'.format(item_cost * TRM, True).replace(',', '.')
            ))

        order_total = shipping_order.get_total()
        grand_total = grand_total + order_total

        print("Total: ${0:.2f}".format(order_total))
        print("")

    print("Grand Total: ${0:.2f}".format(grand_total))

if __name__ == '__main__':
    main()
