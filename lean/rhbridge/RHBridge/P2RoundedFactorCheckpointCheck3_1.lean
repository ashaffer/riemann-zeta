import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk1 :
    P2RoundedFactorCheckpointData.panel3Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix4_eq :
    P2RoundedFactorCheckpointData.panel3Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk1.1

theorem panel3Prefix5_eq :
    P2RoundedFactorCheckpointData.panel3Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk1.2.1

theorem panel3Prefix6_eq :
    P2RoundedFactorCheckpointData.panel3Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk1.2.2.1

theorem panel3Prefix7_eq :
    P2RoundedFactorCheckpointData.panel3Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk1.2.2.2

end RHP2Bridge
