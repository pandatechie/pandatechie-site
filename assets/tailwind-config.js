tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
            "colors": {
                "secondary": "#FF6A3D",
                "surface-container-high": "#232328",
                "outline": "#77777F",
                "vibrant-magenta": "#E8598B",
                "secondary-container": "#5C2A18",
                "surface-container": "#1C1C21",
                "on-surface-variant": "#9C9CA3",
                "electric-azure": "#FF6A3D",
                "background": "#0B0B0D",
                "on-secondary": "#0B0B0D",
                "surface-dim": "#050506",
                "outline-variant": "#2C2C32",
                "surface-container-lowest": "#131316",
                "deep-obsidian": "#FF6A3D",
                "primary-container": "#1C1B1D",
                "surface-variant": "#232328",
                "on-primary": "#0B0B0D",
                "surface-container-highest": "#2A2A30",
                "surface-gray": "#1C1C21",
                "surface-bright": "#0B0B0D",
                "surface-container-low": "#17171B",
                "surface": "#0B0B0D",
                "on-surface": "#F3F3F1",
                "tertiary": "#F3F3F1",
                "on-background": "#F3F3F1",
                "primary": "#F3F3F1",
                "surface-tint": "#9C9CA3"
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
                "display-lg": ["72px", {"lineHeight": "78px", "letterSpacing": "-0.03em", "fontWeight": "800"}]
            }
        }
    }
}
