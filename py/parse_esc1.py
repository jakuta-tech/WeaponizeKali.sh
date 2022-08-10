import json, csv
import glob

with open(glob.glob('[0-9]*_Certipy.json')[0], 'r', encoding='utf-8-sig') as f:
	templates = json.load(f)['Certificate Templates']

data = []
for templ in templates.values():
	if 'Enrollee Supplies Subject' in templ.keys() and templ['Enrollee Supplies Subject']:
		if templ['Client Authentication'] and 'Enrollment Permissions' in templ['Permissions'].keys() and 'Enrollment Rights' in templ['Permissions']['Enrollment Permissions']:
			for perm in templ['Permissions']['Enrollment Permissions']['Enrollment Rights']:
				groups = []
				for group in ['Domain Users', 'Domain Computers', 'Authenticated Users', 'Everyone']:
					if group in perm:
						groups.append(perm)

			template_name = templ['Template Name']
			try:
				authorities = ','.join(templ['Certificate Authorities'])
			except TypeError:
				authorities = ''

			if groups:
				groups = ','.join(groups)
				data.append([template_name, authorities, groups])
				#print(f'"{template_name}","{authorities}","{groups}"')

header = ['TemplateName', 'CertificateAuthorities', 'DangerousGroups']
with open('esc1.csv', 'w') as f:
	writer = csv.writer(f, quoting=csv.QUOTE_ALL)
	writer.writerow(header)
	for row in data:
		writer.writerow(row)
