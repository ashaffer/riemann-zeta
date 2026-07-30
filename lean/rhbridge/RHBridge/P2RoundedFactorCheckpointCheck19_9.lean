import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk9 :
    P2RoundedFactorCheckpointData.panel19Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix36_eq :
    P2RoundedFactorCheckpointData.panel19Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk9.1

theorem panel19Prefix37_eq :
    P2RoundedFactorCheckpointData.panel19Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk9.2.1

theorem panel19Prefix38_eq :
    P2RoundedFactorCheckpointData.panel19Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk9.2.2.1

theorem panel19Prefix39_eq :
    P2RoundedFactorCheckpointData.panel19Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk9.2.2.2

end RHP2Bridge
