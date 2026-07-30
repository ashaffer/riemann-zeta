import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk7 :
    P2RoundedFactorCheckpointData.panel19Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix28_eq :
    P2RoundedFactorCheckpointData.panel19Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk7.1

theorem panel19Prefix29_eq :
    P2RoundedFactorCheckpointData.panel19Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk7.2.1

theorem panel19Prefix30_eq :
    P2RoundedFactorCheckpointData.panel19Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk7.2.2.1

theorem panel19Prefix31_eq :
    P2RoundedFactorCheckpointData.panel19Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk7.2.2.2

end RHP2Bridge
