package com.example.log4j2.json.template.demo;

import lombok.extern.log4j.Log4j2;
import org.apache.logging.log4j.Level;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/index")
@Log4j2
public class dummmyControler {

    @GetMapping("/get")
    public Object getJobDetails() {
        log.info("API started");
        log.log(Level.getLevel("HEALTHCHECK"), "Health checkup process started for settlement engine.");
        log.info("API ended");
        return "API called";
    }
}
