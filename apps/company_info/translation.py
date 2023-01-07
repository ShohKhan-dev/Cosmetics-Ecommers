from modeltranslation.translator import translator, TranslationOptions
from company_info.models import CompanyInfo


class CompanyInfoTranslationOptions(TranslationOptions):
    fields = ['name', 'address', 'city']

translator.register(CompanyInfo, CompanyInfoTranslationOptions)

