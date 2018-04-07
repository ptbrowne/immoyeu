# -*- coding: utf-8 -*-
import scrapy
from immoyeu.items import ImmoyeuItem
import re

def parse_int(s):
    s = re.sub('[^0-9]', '', s)
    return int(s)

def parse_text(t):
    return t

def parse_year(s):
    year = parse_int(s)
    return year if year > 1000 else year + 1900

parsers = {
    'Code postal': ('zipcode', parse_int),
    'Surface habitable (m²)': ('livable_area', parse_int),
    'surface terrain': ('area', parse_int),
    'Nombre de chambre(s)': ('nb_bedrooms', parse_int),
    'Nombre de pièces': ('nb_rooms', parse_int),
    'Nombre de niveaux': ('nb_levels', parse_int),
    'Prix de vente honoraires TTC inclus': ('price', parse_int),
    'Année de construction': ('year', parse_int),
    'Nombre de garage': ('nb_garage', parse_int),
    'Quartier': ('neighborhood', parse_text),
    'Exposition': ('exposition', parse_text)
}

class ScrapepriceSpider(scrapy.Spider):
    name = 'scrapeprice'
    allowed_domains = ['iledyeu-immobilier.com']
    start_urls = ['http://www.iledyeu-immobilier.com/a-vendre/maisons-villas/1']

    def parse(self, response):
        for l in response.css('.pagination a::attr(href)').extract():
            if l.startswith('/'):
                yield scrapy.Request(response.urljoin(l), self.parse)
        for l in response.css('.btn-listing.pull-right::attr(href)').extract():
            yield scrapy.Request(response.urljoin(l), self.parseListing)

    def parseListing(self, response):
        item = ImmoyeuItem()
        
        for id in ['#infos', '#infosfi', '#details']:
            for d in response.css('%s .data' % id):
                k = ''.join(d.css('.termInfos::text').extract()).strip()
                v = ''.join(d.css('.valueInfos::text').extract()).strip()
                if k not in parsers:
                    continue
                name, parser = parsers[k]
                item[name] = parser(v)
        yield item
