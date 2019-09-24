from pages.page_example import PageExample


class PageFactory():
    "PageFactory uses the factory design pattern."

    @staticmethod
    def get_page_object(driver, page_name, base_url=None,trailing_slash_flag=True):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        print("PageName: %s" % page_name)
        if page_name == "page_example":
            test_obj = PageExample(driver=driver, base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        # elif page_name == "redirect":
        #     test_obj = Redirect_Page(base_url=base_url, trailing_slash_flag=trailing_slash_flag)

        return test_obj

