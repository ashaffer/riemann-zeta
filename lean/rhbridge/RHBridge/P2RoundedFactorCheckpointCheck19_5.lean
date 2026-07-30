import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk5 :
    P2RoundedFactorCheckpointData.panel19Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix20_eq :
    P2RoundedFactorCheckpointData.panel19Prefix20 =
      normalizedPrefixTermAtomApprox ⟨20, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk5.1

theorem panel19Prefix21_eq :
    P2RoundedFactorCheckpointData.panel19Prefix21 =
      normalizedPrefixTermAtomApprox ⟨21, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk5.2.1

theorem panel19Prefix22_eq :
    P2RoundedFactorCheckpointData.panel19Prefix22 =
      normalizedPrefixTermAtomApprox ⟨22, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk5.2.2.1

theorem panel19Prefix23_eq :
    P2RoundedFactorCheckpointData.panel19Prefix23 =
      normalizedPrefixTermAtomApprox ⟨23, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk5.2.2.2

end RHP2Bridge
