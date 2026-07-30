import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk1 :
    P2RoundedFactorCheckpointData.panel6Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix4_eq :
    P2RoundedFactorCheckpointData.panel6Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk1.1

theorem panel6Prefix5_eq :
    P2RoundedFactorCheckpointData.panel6Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk1.2.1

theorem panel6Prefix6_eq :
    P2RoundedFactorCheckpointData.panel6Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk1.2.2.1

theorem panel6Prefix7_eq :
    P2RoundedFactorCheckpointData.panel6Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk1.2.2.2

end RHP2Bridge
