cp ../models.py.template ../models.py.template.copy

sh replace_instances.sh ../models.py.template.copy '#ASPECT_1' tf accs maint overall
sh replace_instances.sh ../models.py.template.copy '#ASPECT_2' tf accs maint overall
sh replace_instances.sh ../models.py.template.copy '#ASPECT_3' tf accs maint overall
sh replace_instances.sh ../models.py.template.copy '#ASPECT_4' tf accs maint overall

mv ../models.py.template.copy ../models.py