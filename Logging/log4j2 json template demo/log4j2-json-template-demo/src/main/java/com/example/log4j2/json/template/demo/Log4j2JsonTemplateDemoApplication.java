package com.example.log4j2.json.template.demo;

import com.fasterxml.jackson.core.JsonProcessingException;
import lombok.extern.log4j.Log4j2;
import org.apache.logging.log4j.ThreadContext;
import org.apache.logging.log4j.message.StringMapMessage;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.text.MessageFormat;
import java.util.HashMap;

@SpringBootApplication
@Log4j2
public class Log4j2JsonTemplateDemoApplication {

	public static void main(String[] args) throws JsonProcessingException {
        SpringApplication.run(Log4j2JsonTemplateDemoApplication.class, args);

        ThreadContext.put("ThreadData1", "DummyThreadValue");

        HashMap map = new HashMap();
        map.put("key1", "value1");
        map.put("key2", "value2");
        map.put(MessageFormat.format("My name is {0}", "Rasheed"), "Zain");
        StringMapMessage mapMessage = new StringMapMessage();
        mapMessage.put("key1", "value1");
        mapMessage.put("key2", "value2");

		log.info("'Application started'");
		log.info(map);
		log.info(mapMessage);
	}
}
