import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { Col, Container, Form } from 'react-bootstrap';
import { AiFillPicture } from "react-icons/ai";
import useApiCallback from '../customHooks/useApiCallback';
import Pallete from './Pallete';

export default function WriteTweet({reload}) {

    const [text, setText] = useState("")

    const api = useApiCallback(() => axios.post('http://127.0.0.1:8000/write/', {content : text}),() => reload())



    return (
        <Col sm = {100} className="p-3" style={{backgroundColor : Pallete.secondary, borderRadius: 10}}>
          <textarea value={text} onChange={(event) => setText(event.target.value)} style={{width: "100%", border: 0, height: 100, resize: "none", outline: "none", backgroundColor : Pallete.secondary, color : Pallete.textPrimary, }} placeholder="Escribe tu primer tweet..."></textarea>
          <div className="d-flex justify-content-between align-items-center">
            <AiFillPicture size={30} color={Pallete.textSecondary} class="mt-3">   </AiFillPicture>
            <div onClick={() => {if(text != ""){ api.request(); setText("")}}} style={{padding: "7px 40px", backgroundColor: Pallete.mainColor, color: "white", fontWeight: 600, fontFamily : "Poppins" , borderRadius: 100}}>
              POST
            </div>
          </div>
        </Col>
    )
}
