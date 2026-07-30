import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk2 :
    P2RoundedFactorCheckpointData.panel6Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix8_eq :
    P2RoundedFactorCheckpointData.panel6Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk2.1

theorem panel6Prefix9_eq :
    P2RoundedFactorCheckpointData.panel6Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk2.2.1

theorem panel6Prefix10_eq :
    P2RoundedFactorCheckpointData.panel6Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk2.2.2.1

theorem panel6Prefix11_eq :
    P2RoundedFactorCheckpointData.panel6Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk2.2.2.2

end RHP2Bridge
