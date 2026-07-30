import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk6 :
    P2RoundedFactorCheckpointData.panel11Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix24_eq :
    P2RoundedFactorCheckpointData.panel11Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk6.1

theorem panel11Prefix25_eq :
    P2RoundedFactorCheckpointData.panel11Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk6.2.1

theorem panel11Prefix26_eq :
    P2RoundedFactorCheckpointData.panel11Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk6.2.2.1

theorem panel11Prefix27_eq :
    P2RoundedFactorCheckpointData.panel11Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk6.2.2.2

end RHP2Bridge
