import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk6 :
    P2RoundedFactorCheckpointData.panel2Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix24_eq :
    P2RoundedFactorCheckpointData.panel2Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk6.1

theorem panel2Prefix25_eq :
    P2RoundedFactorCheckpointData.panel2Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk6.2.1

theorem panel2Prefix26_eq :
    P2RoundedFactorCheckpointData.panel2Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk6.2.2.1

theorem panel2Prefix27_eq :
    P2RoundedFactorCheckpointData.panel2Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk6.2.2.2

end RHP2Bridge
