import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk2 :
    P2RoundedFactorCheckpointData.panel25Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix8_eq :
    P2RoundedFactorCheckpointData.panel25Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk2.1

theorem panel25Prefix9_eq :
    P2RoundedFactorCheckpointData.panel25Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk2.2.1

theorem panel25Prefix10_eq :
    P2RoundedFactorCheckpointData.panel25Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk2.2.2.1

theorem panel25Prefix11_eq :
    P2RoundedFactorCheckpointData.panel25Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk2.2.2.2

end RHP2Bridge
