import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk2 :
    P2RoundedFactorCheckpointData.panel30Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix8_eq :
    P2RoundedFactorCheckpointData.panel30Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk2.1

theorem panel30Prefix9_eq :
    P2RoundedFactorCheckpointData.panel30Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk2.2.1

theorem panel30Prefix10_eq :
    P2RoundedFactorCheckpointData.panel30Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk2.2.2.1

theorem panel30Prefix11_eq :
    P2RoundedFactorCheckpointData.panel30Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk2.2.2.2

end RHP2Bridge
