import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk6 :
    P2RoundedFactorCheckpointData.panel20Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix24_eq :
    P2RoundedFactorCheckpointData.panel20Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk6.1

theorem panel20Prefix25_eq :
    P2RoundedFactorCheckpointData.panel20Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk6.2.1

theorem panel20Prefix26_eq :
    P2RoundedFactorCheckpointData.panel20Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk6.2.2.1

theorem panel20Prefix27_eq :
    P2RoundedFactorCheckpointData.panel20Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk6.2.2.2

end RHP2Bridge
