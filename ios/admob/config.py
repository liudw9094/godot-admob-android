def can_build(env, plat):
	return plat=="iphone"

def configure(env):
	if env['platform'] == 'iphone':
		env.AppendUnique(FRAMEWORKPATH=['#modules/admob/lib'])
		env.Append(CPPPATH=['#core'])
