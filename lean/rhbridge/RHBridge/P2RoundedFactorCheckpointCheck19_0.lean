import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk0 :
    P2RoundedFactorCheckpointData.panel19Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix0_eq :
    P2RoundedFactorCheckpointData.panel19Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk0.1

theorem panel19Prefix1_eq :
    P2RoundedFactorCheckpointData.panel19Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk0.2.1

theorem panel19Prefix2_eq :
    P2RoundedFactorCheckpointData.panel19Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk0.2.2.1

theorem panel19Prefix3_eq :
    P2RoundedFactorCheckpointData.panel19Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk0.2.2.2

end RHP2Bridge
