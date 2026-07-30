import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk1 :
    P2RoundedFactorCheckpointData.panel20Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix4_eq :
    P2RoundedFactorCheckpointData.panel20Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk1.1

theorem panel20Prefix5_eq :
    P2RoundedFactorCheckpointData.panel20Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk1.2.1

theorem panel20Prefix6_eq :
    P2RoundedFactorCheckpointData.panel20Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk1.2.2.1

theorem panel20Prefix7_eq :
    P2RoundedFactorCheckpointData.panel20Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk1.2.2.2

end RHP2Bridge
