from __future__ import absolute_import, unicode_literals
import os

from django import VERSION as DJANGO_VERSION
from django.utils.translation import ugettext_lazy as _

DEBUG = True

COMPRESS_ENABLED = False
COMPRESS_OFFLINE = True

SECRET_KEY = "[SECRET_KEY]"
NEVERCACHE_KEY = "[NEVERCACHE_KEY]"


######################
# CARTRIDGE SETTINGS #
######################

# The following settings are already defined in cartridge.shop.defaults
# with default values, but are common enough to be put here, commented
# out, for conveniently overriding. Please consult the settings
# documentation for a full list of settings Cartridge implements:
# http://cartridge.jupo.org/configuration.html#default-settings

SHOP_HANDLER_PAYMENT = 'cartridge.shop.payment.stripe_api.process'

STRIPE_API_KEY = '[STRIPE_API_KEY]'

SHOP_CURRENCY_LOCALE = 'en_US.UTF-8'

SHOP_PRODUCT_SORT_OPTIONS = (('Recently added', '-date_added'), ('Highest rated', '-rating_average'), ('Least expensive', 'unit_price'), ('Most expensive', '-unit_price'))
SHOP_PER_PAGE_CATEGORY = 2
SHOP_USE_WISHLIST = True


######################
# MEZZANINE SETTINGS #
######################

# The following settings are already defined with default values in
# the ``defaults.py`` module within each of Mezzanine's apps, but are
# common enough to be put here, commented out, for conveniently
# overriding. Please consult the settings documentation for a full list
# of settings Mezzanine implements:
# http://mezzanine.jupo.org/docs/configuration.html#default-settings

# ACCOUNTS_NO_USERNAME = True
# ACCOUNTS_VERIFICATION_REQUIRED = True
# ACCOUNTS_APPROVAL_REQUIRED = False


# Controls the ordering and grouping of the admin menu.
#
# ADMIN_MENU_ORDER = (
#     ("Content", ("pages.Page", "blog.BlogPost",
#        "generic.ThreadedComment", (_("Media Library"), "media-library"),)),
#     (_("Shop"), ("shop.Product", "shop.ProductOption", "shop.DiscountCode",
#        "shop.Sale", "shop.Order")),
#     ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
#     ("Users", ("auth.User", "auth.Group",)),
# )

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
#
# DASHBOARD_TAGS = (
#     ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
#     ("comment_tags.recent_comments",),
#     ("mezzanine_tags.recent_actions",),
# )

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

PAGE_MENU_TEMPLATES = (
    (2, ("Left-hand tree"), "pages/menus/tree.html"),
    (3, ("Footer"), "pages/menus/footer.html"),
    (4, ("Shop sidebar"), "pages/menus/shop_sidebar.html"),
)

PAGE_MENU_TEMPLATES_DEFAULT = (2, 3)

# Setting to turn on featured images for blog posts. Defaults to False.
#
# BLOG_USE_FEATURED_IMAGE = True

# If True, the django-modeltranslation will be added to the
# INSTALLED_APPS setting.
USE_MODELTRANSLATION = False

TEMPLATE_ACCESSIBLE_SETTINGS = (
    '__members__', '__methods__', 
    'ACCOUNTS_APPROVAL_REQUIRED', 'ACCOUNTS_VERIFICATION_REQUIRED', 'ADMIN_MENU_COLLAPSED', 'BITLY_ACCESS_TOKEN', 'BLOG_USE_FEATURED_IMAGE', 
    'COMMENTS_DISQUS_SHORTNAME', 'COMMENTS_NUM_LATEST', 'COMMENTS_DISQUS_API_PUBLIC_KEY', 'COMMENTS_DISQUS_API_SECRET_KEY', 'COMMENTS_USE_RATINGS', 
    'DEV_SERVER', 'FORMS_USE_HTML5', 'GRAPPELLI_INSTALLED', 'GOOGLE_ANALYTICS_ID', 'JQUERY_FILENAME', 'JQUERY_UI_FILENAME', 'LOGIN_URL', 'LOGOUT_URL', 
    'SITE_TITLE', 'SITE_TAGLINE', 'USE_L10N', 'USE_MODELTRANSLATION', 'SITEWIDE_NEWSLETTER_PROMO', 'SHOP_USE_WISHLIST', 
    'SHOP_PRODUCT_SORT_OPTIONS', 'SHOP_PER_PAGE_CATEGORY', 'SHOP_USE_WISHLIST', 'SHOP_USE_RELATED_PRODUCTS', 'SHOP_USE_RATINGS', 'SHOP_CHECKOUT_STEPS_SPLIT', 
    'SHOP_USE_UPSELL_PRODUCTS', 'SHOP_PAYMENT_STEP_ENABLED', 
    'SWAGGER_SETTINGS', 'SWAGGER_SCHEME_HTTPS',
    'OLARK_SITE_ID', 
)


########################
# MAIN DJANGO SETTINGS #
########################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en"

# Supported languages
LANGUAGES = (
    ('en', ('English')),
)

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

# The numeric mode to set newly-uploaded files to. The value should be
# a mode you'd pass directly to os.chmod.
FILE_UPLOAD_PERMISSIONS = 0o644


#############
# DATABASES #
#############

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE" : "django.db.backends.postgresql_psycopg2",
        "NAME": "onlineshop",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


###########
# GENERAL #
###########

PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)

CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_APP

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = STATIC_URL + "media/"

MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))

ROOT_URLCONF = "%s.urls" % PROJECT_APP

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_ROOT, "templates")
        ],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "mezzanine.conf.context_processors.settings",
                "mezzanine.pages.context_processors.page",
            ],
            "builtins": [
                "mezzanine.template.loader_tags",
            ],
            "loaders": [
                # "mezzanine.template.loaders.host_themes.Loader",
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]

if DJANGO_VERSION < (1, 9):
    del TEMPLATES[0]["OPTIONS"]["builtins"]


##################
# AWS S3 STORAGE #
##################

AWS_ACCESS_KEY_ID = '[AWS_ACCESS_KEY_ID]'
AWS_SECRET_ACCESS_KEY = '[AWS_SECRET_ACCESS_KEY]'
AWS_STORAGE_BUCKET_NAME = '[AWS_STORAGE_BUCKET_NAME]'

FILEBROWSER_MAX_UPLOAD_SIZE = 50000000 # 50 Megabytes

AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
STATIC_URL = AWS_URL
MEDIA_URL = AWS_URL + 'media/'
ADMIN_MEDIA_PREFIX = AWS_URL + 'admin/'
STATICFILES_STORAGE = 'onlineshop.s3utils.StaticS3BotoStorage'
DEFAULT_FILE_STORAGE = 'onlineshop.s3utils.StaticS3BotoStorage'


################
# APPLICATIONS #
################

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'mezzanine.boot',
    'mezzanine.conf',
    'mezzanine.core',
    'mezzanine.generic',
    'mezzanine.pages',
    'cartridge.shop',
    'mezzanine.blog',
    'mezzanine.forms',
    'mezzanine.galleries',
    'mezzanine.twitter',
    'mezzanine.accounts',
    'corsheaders',
    'rest_framework',
    'rest_framework_api_key',
    'drf_yasg',
    'mezzanine_cartridge_api',
    'widget_tweaks',
    'clear_cache',
    'gunicorn',
)


# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE = (
	# Disable cache middleware in development
    # "mezzanine.core.middleware.UpdateCacheMiddleware",

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    # Uncomment if using internationalisation or localisation
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "cartridge.shop.middleware.ShopMiddleware",
    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",

	# Disable cache middleware in development
    # "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"


#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)


##################
# EMAIL SETTINGS #
##################

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '[EMAIL_HOST]'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
EMAIL_HOST_USER = '[EMAIL_HOST_USER]'
EMAIL_HOST_PASSWORD = '[EMAIL_HOST_PASSWORD]'

DEFAULT_FROM_EMAIL = '[DEFAULT_FROM_EMAIL]'
SERVER_EMAIL = '[DEFAULT_FROM_EMAIL]'


#####################
# REST API SETTINGS #
#####################

#


#########################
# DUMMY CACHING FOR DEV #
#########################

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())


#################
# HEROKU CONFIG #
#################

import mezzanine_heroku
mezzanine_heroku.settings(locals())
