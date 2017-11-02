# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "construction_management"
app_title = "Construction Management"
app_publisher = "Frappé"
app_description = "Control flow of data occuring in Construction of a property"
app_icon = "octicon octicon-home"
app_color = "grey"
app_email = "info@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/construction_management/css/construction_management.css"
# app_include_js = "/assets/construction_management/js/construction_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/construction_management/css/construction_management.css"
# web_include_js = "/assets/construction_management/js/construction_management.js"

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
# get_website_user_home_page = "construction_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "construction_management.install.before_install"
# after_install = "construction_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "construction_management.notifications.get_notification_config"

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
# 		"construction_management.tasks.all"
# 	],
# 	"daily": [
# 		"construction_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"construction_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"construction_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"construction_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "construction_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "construction_management.event.get_events"
# }

