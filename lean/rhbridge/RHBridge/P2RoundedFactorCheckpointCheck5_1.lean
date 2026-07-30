import RHBridge.P2RoundedFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FactorChunk1 :
    P2RoundedFactorCheckpointData.panel5Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨5, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel5Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨5, by decide⟩ := by
  decide +kernel

theorem panel5Prefix4_eq :
    P2RoundedFactorCheckpointData.panel5Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk1.1

theorem panel5Prefix5_eq :
    P2RoundedFactorCheckpointData.panel5Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk1.2.1

theorem panel5Prefix6_eq :
    P2RoundedFactorCheckpointData.panel5Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk1.2.2.1

theorem panel5Prefix7_eq :
    P2RoundedFactorCheckpointData.panel5Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨5, by decide⟩ := by
  exact panel5FactorChunk1.2.2.2

end RHP2Bridge
