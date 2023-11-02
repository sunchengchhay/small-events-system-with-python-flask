from app.extensions import db


class EveCommittee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sys_person_id = db.Column(db.Integer, db.ForeignKey('sys_person.id'))
    eve_event_id = db.Column(db.Integer, db.ForeignKey('eve_event.id'))
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    eve_project_committees = db.relationship(
        'EveProjectCommittee', backref='eve_committee')
    eve_committee_scores = db.relationship(
        'EveCommitteeScore', backref='eve_committee')


class EveGeneration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eve_event_id = db.Column(db.Integer, db.ForeignKey('eve_event.id'))
    sys_department_id = db.Column(
        db.Integer, db.ForeignKey('sys_department.id'))
    name_latin = db.Column(db.String(120))
    year = db.Column(db.String(50), nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    eve_projects = db.relationship('EveProject', backref='eve_generation')

    # one department many results
    eve_results = db.relationship('EveResult', backref='eve_generation')


class EveProjectCommittee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eve_committee_id = db.Column(db.Integer, db.ForeignKey('eve_committee.id'))
    eve_project_shortlist_id = db.Column(
        db.Integer, db.ForeignKey('eve_project_shortlist.id'))
    eve_event_id = db.Column(db.Integer, db.ForeignKey('eve_event.id'))
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)


class EveEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String, nullable=False)
    name_khmer = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    photo_url = db.Column(db.String)
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    eve_committees = db.relationship('EveCommittee', backref='eve_event')
    eve_generations = db.relationship('EveGeneration', backref='eve_event')
    eve_project_committees = db.relationship(
        'EveProjectCommittee', backref='eve_event')
    eve_project_shortlists = db.relationship(
        'EveProjectShortlist', backref='eve_event')
    eve_projects = db.relationship('EveProject', backref='eve_event')
    eve_project_types = db.relationship('EveProjectType', backref='eve_event')
    eve_eval_categories = db.relationship(
        'EveEvalCategory', backref='eve_event')
    eve_eval_criterias = db.relationship(
        'EveEvalCriteria', backref='eve_event')
    eve_rubric_categories = db.relationship(
        'EveRubricCategory', backref='eve_event')
    eve_eval_criteria_rubics = db.relationship(
        'EveEvalCriteriaRubric', backref='eve_event')


class EveProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(100), unique=True)
    eve_event_id = db.Column(db.Integer, db.ForeignKey('eve_event.id'))
    sys_department_id = db.Column(
        db.Integer, db.ForeignKey('sys_department.id'))
    topic = db.Column(db.String)
    eve_project_type_id = db.Column(
        db.Integer, db.ForeignKey('eve_project_type.id'))
    eve_generation_id = db.Column(
        db.Integer, db.ForeignKey('eve_generation.id'))
    member1_name_latin = db.Column(db.String(100), nullable=False)
    member1_name_khmer = db.Column(db.String(100), nullable=False)
    member2_name_latin = db.Column(db.String(100), nullable=True)
    member2_name_khmer = db.Column(db.String(100), nullable=True)
    member3_name_latin = db.Column(db.String(100), nullable=True)
    member3_name_khmer = db.Column(db.String(100), nullable=True)
    member4_name_latin = db.Column(db.String(100), nullable=True)
    member4_name_khmer = db.Column(db.String(100), nullable=True)
    member5_name_latin = db.Column(db.String(100), nullable=True)
    member5_name_khmer = db.Column(db.String(100), nullable=True)
    eve_supervisor_id = db.Column(
        db.Integer, db.ForeignKey('eve_supervisor.id'))
    contact_name = db.Column(db.String(100), nullable=False)
    telegram_number = db.Column(db.String(50))
    email_address = db.Column(db.String(200))
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    # one project one result
    eve_result = db.relationship('EveResult', backref='eve_project')


class EveResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eve_project_shortlist_id = db.Column(
        db.ForeignKey('eve_project_shortlist.id'))
    eve_project_id = db.Column(db.ForeignKey('eve_project.id'))
    eve_generation_id = db.Column(
        db.Integer, db.ForeignKey('eve_generation.id'))
    eve_project_type_id = db.Column(db.ForeignKey(
        'eve_project_type.id'))
    total_score = db.Column(db.Integer)
    is_locked = db.Column(db.Boolean, default=False)
    update_date = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)


class EveProjectShortlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eve_event_id = db.Column(db.Integer, db.ForeignKey('eve_event.id'))
    eve_project_id = db.Column(db.Integer, db.ForeignKey('eve_project.id'))
    eve_project_type_id = db.Column(db.ForeignKey(
        'eve_project_type.id'))    # poster or presentation
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    eve_project_committees = db.relationship(
        'EveProjectCommittee', backref='eve_project_shortlist')
    # one shortlist = one result
    eve_result = db.relationship('EveResult', backref='eve_project_shortlist')
    eve_committee_scores = db.relationship(
        'EveCommitteeScore', backref='eve_project_shortlist')


class EveSupervisor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String(100))
    name_khmer = db.Column(db.String(100))
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    eve_projects = db.relationship('EveProject', backref='supervisor')


class EveProjectType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String(100))
    eve_event_id = db.Column(db.Integer, db.ForeignKey('eve_event.id'))
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    eve_projects = db.relationship('EveProject', backref='eve_project_type')
    eve_project_shortlists = db.relationship(
        'EveProjectShortlist', backref='eve_project_type')
    eve_results = db.relationship(
        'EveResult', backref='eve_project_type')


class EveEvalCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String(100))
    weight = db.Column(db.Float(precision=2))
    eve_event_id = db.Column(db.Integer, db.ForeignKey('eve_event.id'))
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    eve_eval_criterias = db.relationship(
        'EveEvalCriteria', backref='eve_eval_category')


class EveEvalCriteria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String(100))
    eve_eval_category_id = db.Column(
        db.Integer, db.ForeignKey('eve_eval_category.id'))
    eve_event_id = db.Column(db.Integer, db.ForeignKey('eve_event.id'))
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    # alot of rubric in one criteria
    eve_eval_criteria_rubrics = db.relationship(
        'EveEvalCriteriaRubric', backref='eve_eval_criteria')


class EveRubricCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_latin = db.Column(db.String)
    eve_event_id = db.Column(db.Integer, db.ForeignKey('eve_event.id'))
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)


class EveEvalCriteriaRubric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eve_eval_criteria_id = db.Column(
        db.Integer, db.ForeignKey('eve_eval_criteria.id'))
    eve_event_id = db.Column(db.Integer, db.ForeignKey('eve_event.id'))
    score = db.Column(db.Integer)
    eve_rubric_category_id = db.Column(
        db.Integer, db.ForeignKey('eve_rubric_category.id'))
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    eve_committee_scores = db.relationship(
        'EveCommitteeScore', backref='eve_eval_criteria_rubric')


class EveCommitteeScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eve_committee_id = db.Column(db.Integer, db.ForeignKey('eve_committee.id'))
    eve_project_shortlist_id = db.Column(
        db.Integer, db.ForeignKey('eve_project_shortlist.id'))
    eve_event_id = db.Column(db.Integer, db.ForeignKey('eve_event.id'))
    eve_eval_criteria_id = db.Column(
        db.Integer, db.ForeignKey('eve_eval_criteria.id'))
    eve_eval_criteria_rubric_id = db.Column(
        db.Integer, db.ForeignKey('eve_eval_criteria_rubric.id'))
    score = db.Column(db.Float)
    is_locked = db.Column(db.Boolean, default=False)
    created_by = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_by = db.Column(db.Integer, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
