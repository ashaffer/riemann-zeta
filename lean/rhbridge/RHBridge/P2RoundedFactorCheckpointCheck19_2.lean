import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk2 :
    P2RoundedFactorCheckpointData.panel19Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix8_eq :
    P2RoundedFactorCheckpointData.panel19Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk2.1

theorem panel19Prefix9_eq :
    P2RoundedFactorCheckpointData.panel19Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk2.2.1

theorem panel19Prefix10_eq :
    P2RoundedFactorCheckpointData.panel19Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk2.2.2.1

theorem panel19Prefix11_eq :
    P2RoundedFactorCheckpointData.panel19Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk2.2.2.2

end RHP2Bridge
