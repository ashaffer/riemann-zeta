import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk1 :
    P2RoundedFactorCheckpointData.panel7Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix4_eq :
    P2RoundedFactorCheckpointData.panel7Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk1.1

theorem panel7Prefix5_eq :
    P2RoundedFactorCheckpointData.panel7Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk1.2.1

theorem panel7Prefix6_eq :
    P2RoundedFactorCheckpointData.panel7Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk1.2.2.1

theorem panel7Prefix7_eq :
    P2RoundedFactorCheckpointData.panel7Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk1.2.2.2

end RHP2Bridge
