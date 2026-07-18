tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
            "colors": {
                "secondary": "#1e5cb5",
                "surface-container-high": "#e7e8e9",
                "outline": "#79767b",
                "vibrant-magenta": "#DE2F7B",
                "secondary-container": "#70a2ff",
                "surface-container": "#edeeef",
                "on-surface-variant": "#48464a",
                "electric-azure": "#5286E1",
                "background": "#f8f9fa",
                "on-secondary": "#ffffff",
                "surface-dim": "#d9dadb",
                "outline-variant": "#cac5ca",
                "surface-container-lowest": "#ffffff",
                "deep-obsidian": "#181719",
                "primary-container": "#1c1b1d",
                "surface-variant": "#e1e3e4",
                "on-primary": "#ffffff",
                "surface-container-highest": "#e1e3e4",
                "surface-gray": "#F1F3F5",
                "surface-bright": "#f8f9fa",
                "surface-container-low": "#f3f4f5",
                "surface": "#f8f9fa",
                "on-surface": "#191c1d",
                "tertiary": "#000000",
                "on-background": "#191c1d",
                "primary": "#000000",
                "surface-tint": "#605e60"
            },
            "borderRadius": {
                "DEFAULT": "0.125rem",
                "lg": "0.25rem",
                "xl": "0.5rem",
                "full": "0.75rem"
            },
            "spacing": {
                "gutter": "24px",
                "container-max": "1280px",
                "base": "8px",
                "margin-desktop": "64px",
                "margin-mobile": "20px"
            },
            "fontFamily": {
                "headline-lg-mobile": ["Hanken Grotesk"],
                "label-md": ["JetBrains Mono"],
                "label-sm": ["JetBrains Mono"],
                "headline-lg": ["Hanken Grotesk"],
                "body-md": ["Inter"],
                "body-lg": ["Inter"],
                "headline-md": ["Hanken Grotesk"],
                "display-lg": ["Hanken Grotesk"]
            },
            "fontSize": {
                "headline-lg-mobile": ["32px", {"lineHeight": "40px", "fontWeight": "700"}],
                "label-md": ["14px", {"lineHeight": "20px", "letterSpacing": "0.05em", "fontWeight": "500"}],
                "label-sm": ["12px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "500"}],
                "headline-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.01em", "fontWeight": "700"}],
                "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
                "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                "headline-md": ["32px", {"lineHeight": "40px", "fontWeight": "600"}],
                "display-lg": ["64px", {"lineHeight": "72px", "letterSpacing": "-0.02em", "fontWeight": "800"}]
            }
        }
    }
}
