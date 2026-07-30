import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk2 :
    P2RoundedFactorCheckpointData.panel18Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix8_eq :
    P2RoundedFactorCheckpointData.panel18Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk2.1

theorem panel18Prefix9_eq :
    P2RoundedFactorCheckpointData.panel18Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk2.2.1

theorem panel18Prefix10_eq :
    P2RoundedFactorCheckpointData.panel18Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk2.2.2.1

theorem panel18Prefix11_eq :
    P2RoundedFactorCheckpointData.panel18Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk2.2.2.2

end RHP2Bridge
