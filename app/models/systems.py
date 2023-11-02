from app.extensions import db


class SysUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sys_profile_id = db.Column(db.ForeignKey('sys_profile.id'))
    sys_person_id = db.Column(db.ForeignKey('sys_person.id'))
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=1)
    last_login_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)


class SysMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String(100), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)

    sys_sub_menus = db.relationship('SysSubMenu', backref='sys_menu')


class SysSubMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String(100), nullable=False)
    sys_menu_id = db.Column(db.Integer, db.ForeignKey('sys_menu.id'))
    order = db.Column(db.Integer, nullable=False)
    endpoint = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)

    sys_profile_access_rights = db.relationship(
        'SysProfileAccessRight', backref='sys_sub_menu')


class SysProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acronym = db.Column(db.String(64), nullable=False)
    name_latin = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)

    sys_users = db.relationship('SysUser', backref='sys_profile')
    sys_profile_access_rights = db.relationship(
        'SysProfileAccessRight', backref='sys_profile')


class SysRight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acronym = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)

    sys_profile_access_rights = db.relationship(
        'SysProfileAccessRight', backref='sys_right')


class SysProfileAccessRight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sys_profile_id = db.Column(db.Integer, db.ForeignKey('sys_profile.id'))
    sys_sub_menu_id = db.Column(db.Integer, db.ForeignKey('sys_sub_menu.id'))
    sys_right_id = db.Column(db.Integer, db.ForeignKey('sys_right.id'))
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)


class SysPerson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String(100), nullable=False)
    name_khmer = db.Column(db.String(100))
    photo_url = db.Column(db.String)
    sys_gender_id = db.Column(db.ForeignKey('sys_gender.id'))
    sys_nationality_id = db.Column(db.ForeignKey('sys_nationality.id'))
    sys_position_id = db.Column(db.ForeignKey('sys_position.id'))
    sys_organization_id = db.Column(db.ForeignKey('sys_organization.id'))
    sys_department_id = db.Column(db.ForeignKey('sys_department.id'))
    phone = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)

    sys_users = db.relationship('SysUser', backref='sys_person')
    eve_committees = db.relationship('EveCommittee', backref='sys_person')


class SysGender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String(64), nullable=False)
    name_khmer = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)

    sys_persons = db.relationship('SysPerson', backref='sys_gender')


class SysDepartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String, nullable=False)
    name_khmer = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)

    eve_generations = db.relationship(
        'EveGeneration', backref='sys_department')
    eve_projects = db.relationship('EveProject', backref='sys_department')


class SysOrganization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String, nullable=False)
    name_khmer = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)

    sys_persons = db.relationship('SysPerson', backref='sys_organization')


class SysPosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String(100), nullable=False)
    name_khmer = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)

    sys_persons = db.relationship('SysPerson', backref='sys_position')


class SysNationality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String(100), nullable=False)
    name_khmer = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)

    sys_person = db.relationship('SysPerson', backref='sys_nationality')
