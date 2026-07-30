import RHBridge.P2RoundedFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FactorChunk2 :
    P2RoundedFactorCheckpointData.panel20Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨20, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel20Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20Prefix8_eq :
    P2RoundedFactorCheckpointData.panel20Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk2.1

theorem panel20Prefix9_eq :
    P2RoundedFactorCheckpointData.panel20Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk2.2.1

theorem panel20Prefix10_eq :
    P2RoundedFactorCheckpointData.panel20Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk2.2.2.1

theorem panel20Prefix11_eq :
    P2RoundedFactorCheckpointData.panel20Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨20, by decide⟩ := by
  exact panel20FactorChunk2.2.2.2

end RHP2Bridge
