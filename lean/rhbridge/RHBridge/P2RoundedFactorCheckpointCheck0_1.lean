import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk1 :
    P2RoundedFactorCheckpointData.panel0Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix4_eq :
    P2RoundedFactorCheckpointData.panel0Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk1.1

theorem panel0Prefix5_eq :
    P2RoundedFactorCheckpointData.panel0Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk1.2.1

theorem panel0Prefix6_eq :
    P2RoundedFactorCheckpointData.panel0Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk1.2.2.1

theorem panel0Prefix7_eq :
    P2RoundedFactorCheckpointData.panel0Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk1.2.2.2

end RHP2Bridge
