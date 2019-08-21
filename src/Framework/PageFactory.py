class PageFactory():
    "PageFactory uses the factory design pattern."

    @staticmethod
    def get_page_object(page_name,base_url=None,trailing_slash_flag=True):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        # if page_name == "main page":
        #     test_obj = Main_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        # elif page_name == "redirect":
        #     test_obj = Redirect_Page(base_url=base_url, trailing_slash_flag=trailing_slash_flag)

        return test_obj

