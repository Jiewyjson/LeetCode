USER_PROFILE_PUBLIC_QUERY = """\n
query userProfilePublicProfile($userSlug: String!) {\n
  userProfilePublicProfile(userSlug: $userSlug) {\n
    haveFollowed\n
    siteRanking\n
    profile {\n
      userSlug\n
      realName\n
      aboutMe\n
      asciiCode\n
      userAvatar\n
      gender\n
      websites\n
      skillTags\n
      ipRegion\n
      birthday\n
      location\n
      useDefaultAvatar\n
      github\n
      school: schoolV2 {\n
        schoolId\n
        logo\n
        name\n
      }\n
      company: companyV2 {\n
        id\n
        logo\n
        name\n
      }\n
      job\n
      globalLocation {\n
        country\n
        province\n
        city\n
        overseasCity\n
      }\n
      socialAccounts {\n
        provider\n
        profileUrl\n
      }\n
      skillSet {\n
        langLevels {\n
          langName\n
          langVerboseName\n
          level\n
        }\n
        topics {\n
          slug\n
          name\n
          translatedName\n
        }\n
        topicAreaScores {\n
          score\n
          topicArea {\n
            name\n
            slug\n
          }\n
        }\n
      }\n
    }\n
    educationRecordList {\n
      unverifiedOrganizationName\n
    }\n
    occupationRecordList {\n
      unverifiedOrganizationName\n
      jobTitle\n
    }\n
  }\n
}\n
"""