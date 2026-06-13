import flet as ft

def main(page: ft.Page):
    page.title = "Welcome To My Portfolio"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    
    # --- Theme Configurations ---
    PRIMARY_COLOR = ft.colors.BLUE_400
    BG_CARD_COLOR = ft.colors.SURFACE_VARIANT

    # --- Navigation Event Handlers ---
    def handle_menu_click(e):
        page.drawer.open = True
        page.drawer.update()

    def handle_drawer_change(e):
        page.drawer.open = False
        page.drawer.update()
        
        index = e.control.selected_index
        if index == 0:
            page.scroll_to(key="aboutme", duration=800, curve=ft.AnimationCurve.EASE_OUT)
        elif index == 1:
            page.scroll_to(key="timeline", duration=800, curve=ft.AnimationCurve.EASE_OUT)
        elif index == 2:
            page.scroll_to(key="blog", duration=800, curve=ft.AnimationCurve.EASE_OUT)
        elif index == 3:
            page.scroll_to(key="matlab", duration=800, curve=ft.AnimationCurve.EASE_OUT)
        elif index == 4:
            page.scroll_to(key="commit", duration=800, curve=ft.AnimationCurve.EASE_OUT)
        elif index == 5:
            page.scroll_to(key="pr", duration=800, curve=ft.AnimationCurve.EASE_OUT)

    def handle_admin_click(e):
        page.snack_bar = ft.SnackBar(ft.Text("Navigating to Admin Console..."))
        page.snack_bar.open = True
        page.update()

    def handle_message_click(e):
        page.snack_bar = ft.SnackBar(ft.Text("Opening Messages/Contact Form..."))
        page.snack_bar.open = True
        page.update()

    def open_github(e):
        page.launch_url("https://github.com/waardeakawa-sys/UNAM-I36991CP-GROUP-10-TOOLBOX/pulls")

    # Helper function to generate PDF interactive cards dynamically
    def create_certificate_card(title, file_name):
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Icon(ft.icons.PICTURE_AS_PDF_ROUNDED, size=40, color=ft.colors.RED_400),
                    ft.Text(title, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, max_lines=2, size=13),
                    ft.Text("Certificate", size=11, color=ft.colors.BLUE_200)
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                alignment=ft.alignment.center,
                padding=10,
                ink=True
            )
        )

    # --- Layout Components ---

    # 1. Header / About Me Section
    about_me_section = ft.Container(
        key="aboutme",
        content=ft.ResponsiveRow([
            ft.Column(
                col={"sm": 12, "md": 7},
                controls=[
                    ft.Text("About Me", style=ft.TextThemeStyle.HEADLINE_LARGE, color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "My name is Aletta Gottlieb, and I am a second-year Electronics and Computer Engineering student. "
                        "During my studies, I participated in a semester project where our team developed an application called BlastMasterPro.\n\n"
                        "In this project, I served as the Project Manager, where I was responsible for coordinating team activities, "
                        "ensuring meetings were conducted as scheduled, and making sure project milestones were completed according to the timeline.\n\n"
                        "The purpose of BlastMasterPro was to assist mining professionals by providing a blasting calculator that simplifies and improves the blasting process.\n\n"
                        "In addition to project management, I have skills in MATLAB, programming, circuit design, and various technical aspects of engineering. "
                        "I am passionate about applying technology and engineering principles to develop practical solutions to real-world problems.",
                        style=ft.TextThemeStyle.BODY_LARGE
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Column(
                col={"sm": 12, "md": 5},
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src="assets/zera.JPG", 
                            fit=ft.ImageFit.CONTAIN,
                            border_radius=12,
                        ),
                        alignment=ft.alignment.center,
                        border_radius=12,
                        padding=10,
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]),
        padding=30,
        bgcolor=BG_CARD_COLOR,
        border_radius=16,
        margin=ft.margin.only(bottom=15)
    )

    # 2. Timeline Section - Fixed for web compatibility
    timeline_section = ft.Container(
        key="timeline",
        content=ft.Column([
            ft.Text("Official Project Timeline", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD),
            ft.Text("13691CP — 14-Week Semester Layout (02 March – 13 June 2026)", style=ft.TextThemeStyle.BODY_SMALL, italic=True),
            ft.Divider(color=ft.colors.OUTLINE),
            
            ft.Text("Project Phases Overview", style=ft.TextThemeStyle.TITLE_MEDIUM, weight=ft.FontWeight.BOLD),
            ft.Column([
                ft.Row([
                    ft.Column([
                        ft.Text("Phase", weight=ft.FontWeight.BOLD, size=12),
                        ft.Text("PHASE 0", size=11),
                        ft.Text("PHASE 1", size=11),
                        ft.Text("PHASE 2", size=11),
                        ft.Text("PHASE 3", size=11),
                        ft.Text("PHASE 4A", size=11),
                        ft.Text("PHASE 4B", size=11),
                    ], expand=2),
                    ft.Column([
                        ft.Text("Weeks / Dates", weight=ft.FontWeight.BOLD, size=12),
                        ft.Text("Wks 1-2", size=11),
                        ft.Text("Wks 3-4", size=11),
                        ft.Text("Wks 5-8", size=11),
                        ft.Text("Wks 9-12", size=11),
                        ft.Text("Wk 13", size=11),
                        ft.Text("Wk 14", size=11),
                    ], expand=2),
                    ft.Column([
                        ft.Text("Core Deliverables", weight=ft.FontWeight.BOLD, size=12),
                        ft.Text("Group formation, GitHub setup", size=11),
                        ft.Text("Pitch Week presentations", size=11),
                        ft.Text("SRS documentation", size=11),
                        ft.Text("UI/UX prototyping", size=11),
                        ft.Text("Live Expo Demo", size=11),
                        ft.Text("Final Sprint", size=11),
                    ], expand=3),
                ], spacing=10)
            ]),
            
            ft.Container(height=15),
            
            ft.Text("Detailed Weekly Schedule", style=ft.TextThemeStyle.TITLE_MEDIUM, weight=ft.FontWeight.BOLD),
            ft.Column([
                ft.Row([
                    ft.Column([
                        ft.Text("Week", weight=ft.FontWeight.BOLD, size=11),
                        ft.Text("1", size=10),
                        ft.Text("2", size=10),
                        ft.Text("3", size=10),
                        ft.Text("4", size=10),
                        ft.Text("5", size=10),
                        ft.Text("6", size=10),
                        ft.Text("7", size=10),
                        ft.Text("8", size=10),
                        ft.Text("9", size=10),
                        ft.Text("10", size=10),
                        ft.Text("11", size=10),
                        ft.Text("12", size=10),
                        ft.Text("13", size=10),
                        ft.Text("14", size=10),
                    ], expand=1),
                    ft.Column([
                        ft.Text("Dates", weight=ft.FontWeight.BOLD, size=11),
                        ft.Text("02–06 Mar", size=10),
                        ft.Text("09–13 Mar", size=10),
                        ft.Text("16–20 Mar", size=10),
                        ft.Text("23–27 Mar", size=10),
                        ft.Text("30 Mar–03 Apr", size=10),
                        ft.Text("06–10 Apr", size=10),
                        ft.Text("13–17 Apr", size=10),
                        ft.Text("20–25 Apr", size=10),
                        ft.Text("27 Apr–01 May", size=10),
                        ft.Text("04–08 May", size=10),
                        ft.Text("11–15 May", size=10),
                        ft.Text("18–30 May", size=10),
                        ft.Text("01–06 Jun", size=10),
                        ft.Text("08–13 Jun", size=10),
                    ], expand=2),
                    ft.Column([
                        ft.Text("Focus Area", weight=ft.FontWeight.BOLD, size=11),
                        ft.Text("Group formation", size=10),
                        ft.Text("Brainstorming ideas", size=10),
                        ft.Text("Pitch Week begins", size=10),
                        ft.Text("Pitch Week closes", size=10),
                        ft.Text("SRS start", size=10),
                        ft.Text("SRS development", size=10),
                        ft.Text("SRS requirements", size=10),
                        ft.Text("SRS submission", size=10),
                        ft.Text("Figma design start", size=10),
                        ft.Text("Core screens design", size=10),
                        ft.Text("Figma completion", size=10),
                        ft.Text("Prototype refinement", size=10),
                        ft.Text("Live Demo", size=10),
                        ft.Text("Final Sprint", size=10),
                    ], expand=3),
                ], spacing=10)
            ], scroll=ft.ScrollMode.AUTO)
        ]),
        padding=20,
        bgcolor=BG_CARD_COLOR,
        border_radius=16,
        margin=ft.margin.only(bottom=15)
    )

    # 3. Technical Blog Section
    blog_section = ft.Container(
        key="blog",
        content=ft.Column([
            ft.Text("Technical Blog / Engineering Logs", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD),
            ft.Divider(color=ft.colors.OUTLINE),
            ft.ListTile(
                leading=ft.Icon(ft.icons.ARTICLE),
                title=ft.Text("Mastering Flet UI Layouts"),
                subtitle=ft.Text("Deep dive into building responsive architectures using Python structures..."),
            ),
            ft.ListTile(
                leading=ft.Icon(ft.icons.ARTICLE),
                title=ft.Text("Understanding Vector Calculus in System Models"),
                subtitle=ft.Text("Analyzing matrices and spatial gradients for engineering setups..."),
            ),
        ]),
        padding=20,
        bgcolor=BG_CARD_COLOR,
        border_radius=16,
        margin=ft.margin.only(bottom=15)
    )

    # 4. Matlab Achievement Hub Section
    matlab_section = ft.Container(
        key="matlab",
        content=ft.Column([
            ft.Text("Matlab Achievement Hub", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD),
            ft.Divider(color=ft.colors.OUTLINE),
            ft.Text("Engineering app instances, RLC parallel resonance analysis profiles, and Simulink control layouts module representations live here.", style=ft.TextThemeStyle.BODY_MEDIUM),
            ft.Container(height=5),
            ft.GridView(
                expand=False,
                runs_count=4,
                max_extent=180,
                child_aspect_ratio=0.95,
                spacing=15,
                run_spacing=15,
                controls=[
                    create_certificate_card("MATLAB Onramp", "certificate1.pdf"),
                    create_certificate_card("Simulink Onramp", "certificate2.pdf"),
                    create_certificate_card("Explore Plots", "certificate3.pdf"),
                    create_certificate_card("Manipulate Matrices", "certificate4.pdf"),
                    create_certificate_card("Vectors & Matrices", "certificate5.pdf"),
                    create_certificate_card("Circuit Simulation", "certificate6.pdf"),
                    create_certificate_card("Matrix Calculations", "certificate7.pdf"),
                    create_certificate_card("Writing Functions", "certificate8.pdf"),
                ]
            )
        ]),
        padding=20,
        bgcolor=BG_CARD_COLOR,
        border_radius=16,
        margin=ft.margin.only(bottom=15)
    )

    # 5. Commit History Section
    commit_section = ft.Container(
        key="commit",
        content=ft.Column([
            ft.Text("Commit History", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD),
            ft.Divider(color=ft.colors.OUTLINE),
            ft.Text("feat: Add Firebase Auth login screen with email/password validation", font_family="monospace", color=ft.colors.GREEN_300),
            ft.Text("feat: Implement Firestore write for daily inspection report submission", font_family="monospace", color=ft.colors.GREEN_300),
            ft.Text("fix: Resolve crash when Firestore query returns an empty collection", font_family="monospace", color=ft.colors.AMBER_300),
            ft.Text("docs: Add Firestore data model section to SRS document", font_family="monospace", color=ft.colors.BLUE_300),
        ]),
        padding=20,
        bgcolor=BG_CARD_COLOR,
        border_radius=16,
        margin=ft.margin.only(bottom=15)
    )

    # 6. Pull Request Logs Section
    pr_section = ft.Container(
        key="pr",
        content=ft.Column([
            ft.Text("Pull Request Logs", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD),
            ft.Divider(color=ft.colors.OUTLINE),
            ft.Row([
                ft.Icon(ft.icons.MERGE_TYPE, color=ft.colors.PURPLE_400),
                ft.Text("PR #12: Merged Phase 2 SRS functional models into documentation main branch", style=ft.TextThemeStyle.BODY_MEDIUM)
            ]),
            ft.Row([
                ft.Icon(ft.icons.MERGE_TYPE, color=ft.colors.PURPLE_400),
                ft.Text("PR #11: Implemented foundational Expo configuration files and initial dependencies", style=ft.TextThemeStyle.BODY_MEDIUM)
            ]),
            ft.Container(height=10),
            ft.ElevatedButton(
                text="View on GitHub",
                icon=ft.icons.LAUNCH,
                color=ft.colors.WHITE,
                bgcolor=ft.colors.BLUE_600,
                on_click=open_github
            )
        ]),
        padding=20,
        bgcolor=BG_CARD_COLOR,
        border_radius=16,
        margin=ft.margin.only(bottom=150)
    )

    # --- Application Shell Configuration ---
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU, on_click=handle_menu_click),
        leading_width=40,
        title=ft.Row([
            ft.CircleAvatar(
                foreground_image_url="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe",
                radius=16
            ),
            ft.Text("Welcome To My Portfolio", weight=ft.FontWeight.W_500)
        ], spacing=10),
        center_title=False,
        bgcolor=ft.colors.SURFACE,
        actions=[
            ft.IconButton(ft.icons.ADMIN_PANEL_SETTINGS_OUTLINED, on_click=handle_admin_click, tooltip="Admin Console"),
        ],
    )

    page.drawer = ft.NavigationDrawer(
        on_change=handle_drawer_change,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(label="Home", icon=ft.icons.HOME),
            ft.NavigationDrawerDestination(label="Timeline", icon=ft.icons.CALENDAR_MONTH),
            ft.NavigationDrawerDestination(label="Engineering logs", icon=ft.icons.BOOKMARK_BORDER),
            ft.NavigationDrawerDestination(label="Matlab hub", icon=ft.icons.ASSESSMENT),
            ft.NavigationDrawerDestination(label="Commit history", icon=ft.icons.HISTORY),
            ft.NavigationDrawerDestination(label="Pull request logs", icon=ft.icons.MERGE_TYPE),
        ]
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.CHAT_BUBBLE_ROUNDED,
        bgcolor=PRIMARY_COLOR,
        on_click=handle_message_click,
        tooltip="Messages"
    )

    page.add(
        ft.SafeArea(
            ft.Container(
                content=ft.Column([
                    about_me_section,
                    timeline_section,
                    blog_section,
                    matlab_section,
                    commit_section,
                    pr_section
                ], spacing=10),
                padding=10
            )
        )
    )

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
