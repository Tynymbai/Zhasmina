from django import forms
from .models import *


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Фамилия'
        self.fields['Email'].widget.attrs['placeholder'] = 'Рабочая почта'
        self.fields['subject'].widget.attrs['placeholder'] = 'Введите тему'
        self.fields['message'].widget.attrs['placeholder'] = 'Введите сообщение!'

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'Email',
            'subject',
            'message'
        ]
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "Email": "Почта",
            "subject": "Тема",
            "message": "Сообщение"
        }


class JobListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobListingForm, self).__init__(*args, **kwargs)
        self.fields['job_location'].widget.attrs['placeholder'] = 'Алматы, Бостандыкский р-н'
        self.fields['Salary'].widget.attrs['placeholder'] = '100000'
        self.fields['title'].widget.attrs['placeholder'] = 'Информационные системы'
        self.fields['application_deadline'].widget.attrs['placeholder'] = '2023-04-27'

    class Meta:
        model = JobListing
        exclude = ('user', 'image')
        labels = {
            "job_location": "Расположение",
            "published_on": "Дата публикации",
            "title": "Название",
            "company_name": "Название компаний",
            "employment_status": "Занятость",
            "vacancy": "Вакансия",
            "description": "Описание",
            "responsibilities": "Обязанности",
            "experience": "Опыт",
            "Salary": "Зарплата",
            "application_deadline": "Крайний срок(дедлайн)",
        }


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = ApplyJob
        fields = '__all__'
        labels = {
            "file": "Резюме (pdf формат)",
            "name": "ФИО"

        }


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'speciality', 'contacts', 'exp', 'skills']
        labels = {
            "name": "ФИО",
            "speciality": "Специальность",
            "contacts": "Номер телефона",
            "exp": "Опыт",
            "skills": "Навыки"
        }