import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk6 :
    P2RoundedFactorCheckpointData.panel19Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix24_eq :
    P2RoundedFactorCheckpointData.panel19Prefix24 =
      normalizedPrefixTermAtomApprox ⟨24, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk6.1

theorem panel19Prefix25_eq :
    P2RoundedFactorCheckpointData.panel19Prefix25 =
      normalizedPrefixTermAtomApprox ⟨25, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk6.2.1

theorem panel19Prefix26_eq :
    P2RoundedFactorCheckpointData.panel19Prefix26 =
      normalizedPrefixTermAtomApprox ⟨26, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk6.2.2.1

theorem panel19Prefix27_eq :
    P2RoundedFactorCheckpointData.panel19Prefix27 =
      normalizedPrefixTermAtomApprox ⟨27, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk6.2.2.2

end RHP2Bridge
