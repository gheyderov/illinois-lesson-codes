from django.test import TestCase, Client
from django.urls import reverse_lazy
from core.forms import ContactForm, Contact

class ContactViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('contact')
        client = Client()
        cls.response = client.get(cls.url)
        cls.valid_data = {
            'name' : 'admin1',
            'email': 'admin@admin.com',
            'subject' : 'testadsfghfjh',
            'message' : 'test'
        }
        cls.invalid_data = {
            'name' : 'admin1',
            'email': 'adminadmin.com',
            'subject' : 'testadsfghfjh',
            'message' : 'test'
        }
        cls.post_valid = client.post(cls.url, data=cls.valid_data)
        cls.post_invalid = client.post(cls.url, data=cls.invalid_data)


    def test_url(self):
        self.assertEqual(self.url, '/az/contact/')

    def test_request_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_request_template(self):
        self.assertTemplateUsed(self.response, 'contact.html')

    def test_request_context(self):
        self.assertIsInstance(self.response.context['form'], ContactForm)

    def test_post_redirect(self):
        self.assertRedirects(self.post_valid, reverse_lazy('contact'), 302, 200)

    def test_post_errors(self):
        form = self.post_invalid.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('Keçərli e-poçt ünvanı daxil edin.', form.errors['email'])

    def test_post_content(self):
        contact = Contact.objects.first()
        self.assertEqual(contact.name, self.valid_data['name'])
    

    @classmethod
    def tearDownClass(cls) -> None:
        pass