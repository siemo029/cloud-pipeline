/*
 * Copyright 2017-2019 EPAM Systems, Inc. (https://www.epam.com/)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.epam.pipeline.dts.submission.rest.dto;

import com.epam.pipeline.dts.submission.model.execution.SubmissionState;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
public class SubmissionDTO {

    private Long id;
    private Long runId;
    private String runName;
    private String jobId;
    private String jobName;
    private String submissionHost;
    private Integer cores;
    private List<RunParameterDTO> parameters;
    private String dockerImage;
    private String api;
    private String token;
    private String command;
    private Integer coresNumber;
    private SubmissionState state;
}