from Scraper import Scraper
from Course import Course


class TestScraper:
    '''Scraper in Scraper.py'''

    def test_get_page(self):
        """Uses Beautiful Soup to get the HTML from a web page"""
        scraper = Scraper()
        doc = scraper.get_page()
        assert doc is not None

    def test_get_courses(self):
        """Test get_courses"""
        scraper = Scraper()
        course_offerings = scraper.get_courses()
        assert len(course_offerings) > 0  # Ensure courses exist

    def test_make_courses(self):
        """Tests if make_courses() correctly creates Course instances"""
        scraper = Scraper()
        courses = scraper.make_courses()

        assert isinstance(courses, list)
        assert len(courses) > 0  # Ensure courses are being created

        for course in courses:
            assert isinstance(course.title, str)
            assert isinstance(course.schedule, str)  # Fixed from `date` to `schedule`
            assert isinstance(course.description, str)
