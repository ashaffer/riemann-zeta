import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk6 :
    P2RoundedFactorCheckpointData.panel21Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix24_eq :
    P2RoundedFactorCheckpointData.panel21Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk6.1

theorem panel21Prefix25_eq :
    P2RoundedFactorCheckpointData.panel21Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk6.2.1

theorem panel21Prefix26_eq :
    P2RoundedFactorCheckpointData.panel21Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk6.2.2.1

theorem panel21Prefix27_eq :
    P2RoundedFactorCheckpointData.panel21Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk6.2.2.2

end RHP2Bridge
