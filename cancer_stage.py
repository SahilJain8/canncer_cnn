
class cancer_stage:
    def breast_cancer_stage(self ,stage):
        if stage == 1:
            info = "Stage 1 breast cancer means that the cancer is small and only in the breast tissue or it might be found in lymph nodes close to the breast. It is an early stage breast cancer. Staging for breast cancer is very complex"
            treatment = "Surgery is the main treatment for stage I breast cancer.These cancers can be treated with either breast-conserving surgery (BCS; sometimes called lumpectomy or partial mastectomy) or mastectomy"
            return info ,treatment
        if stage == 2:
            info ="Stage 2 breast cancer means that the cancer is either in the breast or in the nearby lymph nodes or both. It is an early stage breast cancer"
            treatment = "Stage II cancers are treated with either breast-conserving surgery (BCS; sometimes called lumpectomy or partial mastectomy) or mastectomy. The nearby lymph nodes will also be checked, either with a sentinel lymph node biopsy (SLNB) or an axillary lymph node dissection (ALND)"
            return info, treatment
        if stage == 3:
            info = "Stage 3 means that the cancer has spread from the breast to lymph nodes close to the breast or to the skin of the breast or to the chest wall.It is also called locally advanced breast cancer."
            treatment = "Treatment for stage 3 breast cancer typically involves surgery, radiation, chemotherapy and other specific therapies, with the order of these treatments tailored to each patient. For many people, treatment will start with chemotherapy, drugs that work throughout the body to kill cancer cells"
            return info, treatment
        else:
            return "e", "f"

    def leukemia(self, stage):
        if stage == 1:
            info = "The blood has too many lymphocytes. The lymph nodes are larger than normal. Other organs are normal size, and the red blood cell and platelet counts are close to normal, too. This stage is medium risk"

            return info
        if stage == 2:
            info = " The blood has too many lymphocytes. The spleen is swollen or enlarged. This is called splenomegaly. The liver may be swollen. This is called hepatomegaly. The lymph nodes may also be larger than normal. Red blood cell and platelet counts are close to normal. This stage is medium risk"

            return info
        if stage == 3:
            info = "The blood has too many lymphocytes. The blood also has too few red blood cells. This is called anemia. The lymph nodes, liver, or spleen may be larger than normal. Platelet counts are close to normal. This stage is high risk."
            return info
        elif stage == 4:
            info = "The blood has too many lymphocytes. It also has too few platelets. This is called thrombocytopenia. The lymph nodes, liver, or spleen may be larger than normal. The blood may have too few red blood cells. This stage is high risk"
            return info

    def lung_cancer(self, stage):
        if stage == 1:
            info = "The cancer is localized to the lungs and has not spread to nearby lymph nodes or other organs. This stage is generally treatable with surgery or radiation therapy."
            return info
        elif stage == 2:
            info = "The cancer has grown larger and may have spread to nearby lymph nodes, but has not spread to other organs. Treatment options may include surgery, radiation therapy, and chemotherapy."
            return info
        elif stage == 3:
            info = "The cancer has spread to nearby tissues or organs, such as the chest wall, diaphragm, or nearby lymph nodes. Treatment options may include a combination of surgery, radiation therapy, and chemotherapy."
            return info
        elif stage == 4:
            info = "The cancer has spread to other parts of the body, such as the liver, brain, or bones. Treatment options may focus on managing symptoms and improving quality of life."
            return info
