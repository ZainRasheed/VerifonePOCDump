package com.example.logback.json.template.demo;

import lombok.extern.log4j.Log4j2;
import lombok.extern.slf4j.Slf4j;
import org.apache.logging.log4j.ThreadContext;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.text.MessageFormat;
import java.util.HashMap;
import java.util.Map;

import static net.logstash.logback.argument.StructuredArguments.entries;
import static net.logstash.logback.argument.StructuredArguments.fields;

@SpringBootApplication
@Log4j2
public class LogbackJsonTemplateDemoApplication {
	public static void main(String[] args) {
//		Logger log = LoggerFactory.getLogger(LogbackJsonTemplateDemoApplication.class);
		SpringApplication.run(LogbackJsonTemplateDemoApplication.class, args);

		MDC.put("key1", "valueee1");
		MDC.put("key2", "valueee2");
		MDC.put("key3", "valueee3");

		ThreadContext.put("kkey1", "value1");
		ThreadContext.put("kkey2", "value2");
		ThreadContext.put("kkey3", "value3");

		log.info("info log");
		log.warn("warn log");
		log.error("error log");
		log.debug("debug log");

		Map<String, Object> map = new HashMap<>();
		map.put("key1", "value1");
		map.put("key2", "value2");
		log.info(fields(map));
		log.info("{\"a\": 1, \"b\": 2}");
//		log.info(map.toString());
//		log.info(map);
	}

}
