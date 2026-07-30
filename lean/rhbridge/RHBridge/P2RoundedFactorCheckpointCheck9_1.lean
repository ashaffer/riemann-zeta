import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk1 :
    P2RoundedFactorCheckpointData.panel9Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix4_eq :
    P2RoundedFactorCheckpointData.panel9Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk1.1

theorem panel9Prefix5_eq :
    P2RoundedFactorCheckpointData.panel9Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk1.2.1

theorem panel9Prefix6_eq :
    P2RoundedFactorCheckpointData.panel9Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk1.2.2.1

theorem panel9Prefix7_eq :
    P2RoundedFactorCheckpointData.panel9Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk1.2.2.2

end RHP2Bridge
