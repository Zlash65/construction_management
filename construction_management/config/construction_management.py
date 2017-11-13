from frappe import _

def get_data():
	return [
		{
			"label": _("Projects"),
			"icon": "fa fa-cubes",
			"items": [
				{
					"type": "doctype",
					"name": "Project",
					"description": _("Project master."),
				},
				{
					"type": "doctype",
					"name": "Task",
					"route": "Tree/Task",
					"description": _("Project activity / task."),
				},
				{
					"type": "doctype",
					"name": "Project Type",
					"description": _("Define Project type."),
				}
			]
		},
		{
			"label": _("Construct"),
			"icon": "fa fa-building",
			"items": [
				{
					"type": "doctype",
					"name": "BOQ",
					"description": _("Construction related BOQ"),
				},
				{
					"type": "doctype",
					"name": "Rate Analysis",
					"description": _("Construction related Rates"),
				}
			]
		},
		{
			"label": _("Configure"),
			"icon": "fa fa-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "UOM",
					"description": _("Unit of Measure"),
				},
				{
					"type": "doctype",
					"name": "Unit Conversion",
					"description": _("Unit Conversion"),
				},
				{
					"type": "doctype",
					"name": "Basic Rates",
					"description": _("Standard Rates"),
				},
			]
		}
	]