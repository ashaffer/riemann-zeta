import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk2 :
    P2RoundedFactorCheckpointData.panel10Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix8_eq :
    P2RoundedFactorCheckpointData.panel10Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk2.1

theorem panel10Prefix9_eq :
    P2RoundedFactorCheckpointData.panel10Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk2.2.1

theorem panel10Prefix10_eq :
    P2RoundedFactorCheckpointData.panel10Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk2.2.2.1

theorem panel10Prefix11_eq :
    P2RoundedFactorCheckpointData.panel10Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk2.2.2.2

end RHP2Bridge
