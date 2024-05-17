import reflex as rx 
import link_bio.styles.styles as styles



def link_button(title: str,body: str,image: str, url: str) -> rx.Component:
    return rx.link(
                rx.button(
                    rx.hstack(
                        rx.image(
                            src=image,
                            width=styles.Size.BIG.value,
                            height=styles.Size.BIG.value,
                           
                        ),
                        rx.vstack(
                            rx.text(title,style=styles.button_tittle_style),
                            rx.text(body,style=styles.button_body_style),
                            spacing="0",
                            align_items="start",
                            margin=0,
                        ),
                        align_items="center",
                    ),
               
                ),
                href=url,
                is_external=True,
                width="100%",
                align="center",
                height="auto",
                    )


            
               
                   
                    
                   
               
               
                    
                    
                   
                    
                  
                
              
           
        
       
     
       
       
      
 



