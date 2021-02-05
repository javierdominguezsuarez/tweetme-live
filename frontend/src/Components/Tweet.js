import React from 'react'
import { Col } from 'react-bootstrap'
import { AiOutlineHeart, AiFillHeart, AiOutlineRetweet } from "react-icons/ai";
import Pallete from './Pallete'

export default function Tweet({obj}) {
    return (
        <Col sm = {100} className="p-3 mt-3 text-left" style={{backgroundColor : Pallete.secondary, borderRadius: 10 }}>

            <div class=" d-flex align-items-center">


                <img src="https://concepto.de/wp-content/uploads/2018/08/persona-e1533759204552.jpg" style={{width: 40, height : 40,  objectFit: "cover", borderRadius: "50%"}}></img>
                <h5 style={{fontWeight: 600, color: Pallete.mainColor}} className="ml-3">Jose Peña Seco</h5>
                <p className="ml-3 mt-2" style={{color: Pallete.textSecondary}}>@josepenaseco</p>
            </div>
            <p class="mt-2" style={{fontFamily: "Poppins", color: Pallete.textPrimary}}>
                {obj.content}
            </p>

            <div>
                <AiOutlineHeart size={25} color={Pallete.textSecondary}/>
                <AiOutlineRetweet size={25} className="ml-4" color={Pallete.textSecondary}/>
            </div>
        </Col>
    )
}
