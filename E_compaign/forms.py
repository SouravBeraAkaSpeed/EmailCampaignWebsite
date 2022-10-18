from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out', 'placeholder': '', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
            'placeholder': '',
            'id': 'password',
        }
    ))


class UploadFileForm(forms.Form):

    smtp = forms.FileField(widget=forms.FileInput(
        attrs={
            'class': 'item_form w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
            'id': 'smtp',
            'type': 'file',
            'name': 'smtp',


        }
    ), required=False)
    data = forms.FileField(widget=forms.FileInput(
        attrs={
            'class': 'item_form w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
            'id': 'data',
            'type': 'file',
            'name': 'data',

        }
    ), required=False)
    links = forms.FileField(widget=forms.FileInput(
        attrs={
            'class': 'item_form w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
            'id': 'links',
            'type': 'file',
            'name': 'links',

        }
    ), required=False)
    content = forms.FileField(widget=forms.FileInput(
        attrs={
            'class': 'item_form w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
            'id': 'content',
            'type': 'file',
            'name': 'content',
            'multiple': True,

        }
    ), required=False)
    attachments = forms.FileField(widget=forms.FileInput(
        attrs={
            'class': 'item_form w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
            'id': 'attachments',
            'type': 'file',
            'name': 'attachments',
            'multiple': True,

        }
    ), required=False)
    subjects = forms.FileField(widget=forms.FileInput(
        attrs={
            'class': 'item_form w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
            'id': 'subjects',
            'type': 'file',
            'name': 'subjects',

        }
    ), required=False)
    proxies = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'item_form w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
            'placeholder': 'http://example-proxy.com:8000',
            'type': 'text',
            'id': 'proxies',
            'name': 'proxies',

        }
    ))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'item_form w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
            'placeholder': '+91 8738738890',
            'type': 'text',
            'id': 'phone',
            'name': 'phone',

        }
    ))
    time_delay = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'item_form w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
            'placeholder': '30',
            'type': 'number',
            'id': 'time_delay',
            'name': 'time_delay',

        }
    ))

    instance = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'item_form w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
            'placeholder': '2',
            'type': 'number',
            'id': 'instance',
            'name': 'instance',

        }
    ))
