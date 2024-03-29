# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "pk_taxation"
app_title = "PK Taxation"
app_publisher = "Betalogics"
app_description = "App Pakistan taxation fields"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "avaiskhatri@betalogics.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pk_taxation/css/pk_taxation.css"
# app_include_js = "/assets/pk_taxation/js/pk_taxation.js"

# include js, css files in header of web template
# web_include_css = "/assets/pk_taxation/css/pk_taxation.css"
# web_include_js = "/assets/pk_taxation/js/pk_taxation.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "pk_taxation.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pk_taxation.install.before_install"
# after_install = "pk_taxation.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pk_taxation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pk_taxation.tasks.all"
# 	],
# 	"daily": [
# 		"pk_taxation.tasks.daily"
# 	],
# 	"hourly": [
# 		"pk_taxation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pk_taxation.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pk_taxation.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pk_taxation.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pk_taxation.event.get_events"
# }

fixtures = [
       {
         "dt": "Custom Field", 
         "filters":[["name", "in", [
              'Item-pct_code',
              'Company-ntn','Company-strn','Company-cnic',
              'Supplier-cnic', 'Supplier-ntn', 'Supplier-strn',
              'Purchase Order-cnic', 'Purchase Order-ntn', 'Purchase Order-strn',
              'Purchase Receipt-cnic', 'Purchase Receipt-ntn', 'Purchase Receipt-strn',
              'Purchase Order Item-pct_code',
              'Purchase Receipt Item-pct_code',
              'Purchase Invoice-ntn', 'Purchase Invoice-strn', 'Purchase Invoice-cnic',
              'Purchase Invoice Item-pct_code',
              'Customer-cnic', 'Customer-ntn', 'Customer-strn',
              'Quotation Item-pct_code',
              'Sales Order-cnic', 'Sales Order-ntn', 'Sales Order-strn',
              'Sales Order Item-pct_code',
              'Delivery Note Item-pct_code',
              'Sales Invoice-cnic', 'Sales Invoice-ntn', 'Sales Invoice-strn',
              'Sales Invoice Item-pct_code',
              'Employee-cnic','Employee-cnic_issue_date','Employee-cnic_expiry_date'
             ]]]
      }
]