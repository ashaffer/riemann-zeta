import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk10 :
    P2RoundedFactorCheckpointData.panel19Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix40_eq :
    P2RoundedFactorCheckpointData.panel19Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk10.1

theorem panel19Prefix41_eq :
    P2RoundedFactorCheckpointData.panel19Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk10.2.1

theorem panel19Prefix42_eq :
    P2RoundedFactorCheckpointData.panel19Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk10.2.2.1

theorem panel19Prefix43_eq :
    P2RoundedFactorCheckpointData.panel19Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk10.2.2.2

end RHP2Bridge
